import { Tooltip as BaseTooltip } from '@base-ui/react/tooltip';
import type { ReactNode } from 'react';
import './Tooltip.css';

export interface SettingsTooltipProps {
  content: ReactNode;
  children: React.ReactElement;
}

export function SettingsTooltip({ content, children }: SettingsTooltipProps) {
  return (
    <BaseTooltip.Root>
      <BaseTooltip.Trigger className="settings-tooltip-trigger" delay={0} render={<span />}>
        {children}
      </BaseTooltip.Trigger>
      <BaseTooltip.Portal>
        <BaseTooltip.Positioner sideOffset={4}>
          <BaseTooltip.Popup className="settings-tooltip-popup">
            {content}
            <BaseTooltip.Arrow className="settings-tooltip-arrow" />
          </BaseTooltip.Popup>
        </BaseTooltip.Positioner>
      </BaseTooltip.Portal>
    </BaseTooltip.Root>
  );
}
