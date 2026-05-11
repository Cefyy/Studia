import { useState } from 'react';
import { Combobox as BaseCombobox } from '@base-ui/react/combobox';
import './Combobox.css';

export interface ComboboxOption {
  id: string;
  label: string;
}

export interface SettingsComboboxProps {
  label: string;
  options: ComboboxOption[];
}

export function SettingsCombobox({ label, options }: SettingsComboboxProps) {
  const [query, setQuery] = useState('');
  const [selectedValues, setSelectedValues] = useState<string[]>(['react', 'typescript']);

  const filteredOptions = query === '' 
    ? options 
    : options.filter(opt => opt.label.toLowerCase().includes(query.toLowerCase()));

  return (
    <div className="settings-combobox-container">
      <label className="settings-field-label">{label}</label>
      
      <BaseCombobox.Root 
        value={selectedValues}
        onValueChange={(val) => setSelectedValues(val as string[])}
        multiple
      >
        <div className="settings-combobox-control">
          {selectedValues.map(val => {
            const option = options.find(o => o.id === val);
            if (!option) return null;
            return (
              <span key={val} className="settings-combobox-tag">
                {option.label}
                <button 
                  type="button" 
                  className="settings-combobox-tag-remove"
                  onClick={(e) => {
                    e.stopPropagation();
                    setSelectedValues(prev => prev.filter(v => v !== val));
                  }}
                >
                  x
                </button>
              </span>
            );
          })}
          <BaseCombobox.Input 
            className="settings-combobox-input" 
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onBlur={() => setQuery('')}
            placeholder={selectedValues.length === 0 ? "Select options..." : ""}
          />
        </div>
        
        <BaseCombobox.Portal>
          <BaseCombobox.Positioner sideOffset={4}>
            <BaseCombobox.Popup className="settings-combobox-popup">
              {filteredOptions.length === 0 ? (
                <div className="settings-combobox-empty">No options found</div>
              ) : (
                filteredOptions.map((option) => (
                  <BaseCombobox.Item key={option.id} value={option.id} className="settings-combobox-item">
                    <span>{option.label}</span>
                    <BaseCombobox.ItemIndicator className="settings-combobox-indicator">✓</BaseCombobox.ItemIndicator>
                  </BaseCombobox.Item>
                ))
              )}
            </BaseCombobox.Popup>
          </BaseCombobox.Positioner>
        </BaseCombobox.Portal>
      </BaseCombobox.Root>
    </div>
  );
}
