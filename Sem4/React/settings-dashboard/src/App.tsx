import { useState } from 'react';
import { User, Bell, Palette, AlertTriangle, Info } from 'lucide-react';
import { SettingsAccordion, SettingsAccordionItem } from './components/Accordion/SettingsAccordion';
import { SettingsSwitch } from './components/Switch/SettingsSwitch';
import { SettingsSelect } from './components/Select/SettingsSelect';
import { SettingsSlider } from './components/Slider/SettingsSlider';
import { SettingsDialog } from './components/Dialog/SettingsDialog';
import { SettingsRadioGroup } from './components/Radio/SettingsRadio';
import { SettingsCombobox } from './components/Combobox/SettingsCombobox';
import { SettingsTooltip } from './components/Tooltip/SettingsTooltip';
import { SettingsInput } from './components/Input/SettingsInput';
import './App.css';

const SKILLS_OPTIONS = [
  { id: 'react', label: 'React' },
  { id: 'typescript', label: 'TypeScript' },
  { id: 'vue', label: 'Vue.js' },
  { id: 'angular', label: 'Angular' },
  { id: 'node', label: 'Node.js' },
  { id: 'python', label: 'Python' },
  { id: 'java', label: 'Java' },
  { id: 'csharp', label: 'C#' },
  { id: 'aws', label: 'AWS' },
  { id: 'docker', label: 'Docker' },
  { id: 'kubernetes', label: 'Kubernetes' },
];

const LANGUAGE_OPTIONS = [
  { value: 'en', label: 'en' },
  { value: 'pl', label: 'pl' },
  { value: 'es', label: 'es' },
  { value: 'de', label: 'de' },
];

const DIGEST_OPTIONS = [
  { value: 'instant', label: 'Instant' },
  { value: 'daily', label: 'Daily' },
  { value: 'weekly', label: 'Weekly' },
];

function App() {
  const [fontSize, setFontSize] = useState(16);
  
  return (
    <div className="app-container" style={{ fontSize: `${fontSize}px` }}>
      <header className="app-header">
        <h1>Settings Dashboard</h1>
      </header>

      <main className="app-main">
        <SettingsAccordion>
          
          <SettingsAccordionItem 
            value="profile" 
            title="Profile" 
            icon={<User size={18} color="#4f46e5" />}
          >
            <div className="section-content">
              <SettingsInput 
                label="Name" 
                defaultValue="John Doe"
                icon={
                  <SettingsTooltip content="Your full name as displayed to other users.">
                    <span style={{ display: 'inline-flex', alignItems: 'center' }}>
                      <Info size={14} />
                    </span>
                  </SettingsTooltip>
                }
              />
              <SettingsInput 
                label="Email" 
                defaultValue="john@example.com" 
                type="email"
              />
              <SettingsCombobox 
                label="Skills & Interests" 
                options={SKILLS_OPTIONS} 
              />
            </div>
          </SettingsAccordionItem>

          <SettingsAccordionItem 
            value="notifications" 
            title="Notifications" 
            icon={<Bell size={18} color="#eab308" />}
          >
            <div className="section-content">
              <div className="switches-group">
                <SettingsSwitch 
                  label="Email notifications" 
                  description="Receive updates via email"
                  defaultChecked
                />
                <SettingsSwitch 
                  label="Push notifications" 
                  description="Get browser push alerts"
                />
                <SettingsSwitch 
                  label="Marketing emails" 
                  description="Receive promotional content"
                />
              </div>

              <SettingsRadioGroup 
                label="Digest frequency"
                defaultValue="daily"
                options={DIGEST_OPTIONS}
              />
            </div>
          </SettingsAccordionItem>

          <SettingsAccordionItem 
            value="appearance" 
            title="Appearance" 
            icon={<Palette size={18} color="#f43f5e" />}
          >
            <div className="section-content">
              <SettingsSelect 
                label="Language" 
                defaultValue="en"
                options={LANGUAGE_OPTIONS}
              />
              
              <div style={{ marginTop: 24, maxWidth: '400px' }}>
                <SettingsSlider 
                  label="Font size" 
                  min={12} 
                  max={24} 
                  value={fontSize} 
                  onChange={(v) => {
                    setFontSize(Array.isArray(v) ? v[0] : v);
                  }}
                  formatValue={(v) => `${v}px`}
                />
              </div>
            </div>
          </SettingsAccordionItem>

          <SettingsAccordionItem 
            value="danger" 
            title="Danger Zone" 
            icon={<AlertTriangle size={18} color="#f59e0b" />}
          >
            <div className="section-content">
              <p className="danger-text">
                Once you delete your account, there is no going back. Please be certain.
              </p>
              
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <SettingsDialog
                  title="Delete Account"
                  description="Are you sure you want to permanently delete your account? This action cannot be undone and you will lose all your data."
                  confirmLabel="Delete Account"
                  trigger={<button className="btn-danger">Delete Account</button>}
                  onConfirm={() => console.log('Account deleted')}
                />
                <SettingsTooltip content="This will permanently erase all your data.">
                  <div style={{ cursor: 'help', display: 'flex', alignItems: 'center', color: '#6b7280' }}>
                    <Info size={16} />
                  </div>
                </SettingsTooltip>
              </div>
            </div>
          </SettingsAccordionItem>

        </SettingsAccordion>
      </main>
    </div>
  );
}

export default App;
