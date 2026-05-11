import { RadioGroup as BaseRadioGroup } from '@base-ui/react/radio-group';
import { Radio as BaseRadio } from '@base-ui/react/radio';
import { forwardRef } from 'react';
import './Radio.css';

export interface RadioOption {
  value: string;
  label: string;
}

export interface SettingsRadioGroupProps extends React.HTMLAttributes<HTMLDivElement> {
  label: string;
  options: RadioOption[];
  defaultValue?: string;
}

export const SettingsRadioGroup = forwardRef<HTMLDivElement, SettingsRadioGroupProps>(
  ({ label, options, ...props }, ref) => {
    return (
      <div className="settings-radio-group-container">
        <label className="settings-radio-group-label">{label}</label>
        <BaseRadioGroup ref={ref} className="settings-radio-group" {...props}>
          {options.map((option) => (
            <label key={option.value} className="settings-radio-label">
              <BaseRadio.Root value={option.value} className="settings-radio-item">
                <BaseRadio.Indicator className="settings-radio-indicator" />
              </BaseRadio.Root>
              {option.label}
            </label>
          ))}
        </BaseRadioGroup>
      </div>
    );
  }
);

SettingsRadioGroup.displayName = 'SettingsRadioGroup';
