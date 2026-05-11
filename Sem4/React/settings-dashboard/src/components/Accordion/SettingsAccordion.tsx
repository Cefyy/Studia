import { Accordion as BaseAccordion } from '@base-ui/react/accordion';
import type { ReactNode } from 'react';
import './Accordion.css';

export interface SettingsAccordionProps {
  children: ReactNode;
}

export function SettingsAccordion({ children }: SettingsAccordionProps) {
  return (
    <BaseAccordion.Root className="settings-accordion" defaultValue={["profile"]}>
      {children}
    </BaseAccordion.Root>
  );
}

export interface SettingsAccordionItemProps {
  value: string;
  icon?: ReactNode;
  title: string;
  children: ReactNode;
}

export function SettingsAccordionItem({ value, icon, title, children }: SettingsAccordionItemProps) {
  return (
    <BaseAccordion.Item className="settings-accordion-item" value={value}>
      <BaseAccordion.Header className="settings-accordion-header">
        <BaseAccordion.Trigger className="settings-accordion-trigger">
          <div className="settings-accordion-title">
            {icon}
            <span>{title}</span>
          </div>
          <span className="settings-accordion-chevron">✕</span>
        </BaseAccordion.Trigger>
      </BaseAccordion.Header>
      <BaseAccordion.Panel className="settings-accordion-panel">
        <div className="settings-accordion-content">
          {children}
        </div>
      </BaseAccordion.Panel>
    </BaseAccordion.Item>
  );
}
