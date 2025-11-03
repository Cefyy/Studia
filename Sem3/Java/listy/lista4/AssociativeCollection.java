interface AssociativeCollection extends Cloneable, AssocColl {
    void del(String k);

    int size();

    @Override
    default String defaultToString() {
        String[] keys = names();
        if (keys == null || keys.length == 0) {
            return "{collection is empty}";
        }

        String[] pairs = new String[keys.length];
        for (int i = 0; i < keys.length; i++) {
            pairs[i] = keys[i] + "->" + get(keys[i]);
        }

        return "{size=" + size() + ", items=[" + String.join("; ", pairs) + "]}";
    }
}
