import { forwardRef } from 'react';
import { Switch as BaseSwitch } from '@base-ui/react/switch';
import './Switch.css';

export interface SettingsSwitchProps extends React.ComponentPropsWithoutRef<typeof BaseSwitch.Root> {
  label: string;
  description?: string;
}

export const SettingsSwitch = forwardRef<HTMLButtonElement, SettingsSwitchProps>(
  ({ label, description, ...props }, ref) => {
    return (
      <div className="settings-switch-container">
        <div className="settings-switch-text">
          <label className="settings-switch-label">{label}</label>
          {description && <span className="settings-switch-description">{description}</span>}
        </div>
        <BaseSwitch.Root ref={ref} className="settings-switch-root" {...props}>
          <BaseSwitch.Thumb className="settings-switch-thumb" />
        </BaseSwitch.Root>
      </div>
    );
  }
);

SettingsSwitch.displayName = 'SettingsSwitch';
