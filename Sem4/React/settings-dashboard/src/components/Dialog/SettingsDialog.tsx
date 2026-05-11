import { Dialog as BaseDialog } from '@base-ui/react/dialog';
import type { ReactNode } from 'react';
import './Dialog.css';

export interface SettingsDialogProps {
  trigger: React.ReactElement;
  title: string;
  description: ReactNode;
  confirmLabel?: string;
  cancelLabel?: string;
  onConfirm: () => void;
}

export function SettingsDialog({
  trigger,
  title,
  description,
  confirmLabel = 'Confirm',
  cancelLabel = 'Cancel',
  onConfirm
}: SettingsDialogProps) {
  return (
    <BaseDialog.Root>
      <BaseDialog.Trigger render={trigger} />
      <BaseDialog.Portal>
        <BaseDialog.Backdrop className="settings-dialog-backdrop" />
        <BaseDialog.Popup className="settings-dialog-popup">
          <BaseDialog.Title className="settings-dialog-title">{title}</BaseDialog.Title>
          <BaseDialog.Description className="settings-dialog-description">
            {description}
          </BaseDialog.Description>
          <div className="settings-dialog-actions">
            <BaseDialog.Close className="settings-btn-cancel">
              {cancelLabel}
            </BaseDialog.Close>
            <BaseDialog.Close className="settings-btn-confirm" onClick={onConfirm}>
              {confirmLabel}
            </BaseDialog.Close>
          </div>
        </BaseDialog.Popup>
      </BaseDialog.Portal>
    </BaseDialog.Root>
  );
}
