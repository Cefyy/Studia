import { Input as BaseInput } from '@base-ui/react/input';
import { forwardRef } from 'react';
import './Input.css';

export interface SettingsInputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label: string;
  icon?: React.ReactNode;
}

export const SettingsInput = forwardRef<HTMLInputElement, SettingsInputProps>(
  ({ label, icon, ...props }, ref) => {
    return (
      <div className="settings-input-container">
        <label className="settings-field-label">
          {label}
          {icon && <span className="settings-field-icon">{icon}</span>}
        </label>
        <BaseInput ref={ref} className="settings-input-root" {...props} />
      </div>
    );
  }
);
SettingsInput.displayName = 'SettingsInput';
