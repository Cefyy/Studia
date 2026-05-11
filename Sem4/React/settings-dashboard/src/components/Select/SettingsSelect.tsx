import { Select as BaseSelect } from '@base-ui/react/select';
import { forwardRef } from 'react';
import './Select.css';

export interface SelectOption {
  value: string;
  label: string;
}

export interface SettingsSelectProps {
  label: string;
  options: SelectOption[];
  defaultValue?: string;
  value?: string;
  onChange?: (value: string | null) => void;
}

export const SettingsSelect = forwardRef<HTMLButtonElement, SettingsSelectProps>(
  ({ label, options, defaultValue, value, onChange }, ref) => {
    return (
      <div className="settings-select-container">
        <label className="settings-field-label">{label}</label>
        <BaseSelect.Root
          defaultValue={defaultValue}
          value={value}
          onValueChange={onChange}
        >
          <BaseSelect.Trigger className="settings-select-trigger" ref={ref}>
            <BaseSelect.Value placeholder="Select..." />
            <span className="settings-select-icon">↕</span>
          </BaseSelect.Trigger>
          <BaseSelect.Portal>
            <BaseSelect.Positioner sideOffset={4}>
              <BaseSelect.Popup className="settings-select-popup">
                {options.map((option) => (
                  <BaseSelect.Item
                    key={option.value}
                    value={option.value}
                    className="settings-select-item"
                  >
                    <BaseSelect.ItemText>{option.label}</BaseSelect.ItemText>
                    <BaseSelect.ItemIndicator className="settings-select-indicator">✓</BaseSelect.ItemIndicator>
                  </BaseSelect.Item>
                ))}
              </BaseSelect.Popup>
            </BaseSelect.Positioner>
          </BaseSelect.Portal>
        </BaseSelect.Root>
      </div>
    );
  }
);
SettingsSelect.displayName = 'SettingsSelect';
