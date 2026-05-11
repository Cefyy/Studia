import { Slider as BaseSlider } from '@base-ui/react/slider';
import { forwardRef } from 'react';
import './Slider.css';

export interface SettingsSliderProps {
  label: string;
  min: number;
  max: number;
  step?: number;
  value: number;
  onChange: (value: number | number[]) => void;
  formatValue?: (value: number) => string;
}

export const SettingsSlider = forwardRef<HTMLDivElement, SettingsSliderProps>(
  ({ label, min, max, step = 1, value, onChange, formatValue = (v) => v.toString() }, ref) => {
    return (
      <div className="settings-slider-container">
        <div className="settings-slider-header">
          <label className="settings-field-label">{label}</label>
          <span className="settings-slider-value">{formatValue(value)}</span>
        </div>
        <BaseSlider.Root
          ref={ref}
          className="settings-slider-root"
          min={min}
          max={max}
          step={step}
          value={value}
          onValueChange={onChange}
        >
          <BaseSlider.Control className="settings-slider-control">
            <BaseSlider.Track className="settings-slider-track">
              <BaseSlider.Indicator className="settings-slider-indicator" />
            </BaseSlider.Track>
            <BaseSlider.Thumb className="settings-slider-thumb" />
          </BaseSlider.Control>
        </BaseSlider.Root>
      </div>
    );
  }
);
SettingsSlider.displayName = 'SettingsSlider';
