import Skill from './Skill';
import './SkillsList.css';

interface SkillsListProps {
    skills: string[];
}

export default function SkillsList({ skills }: SkillsListProps) {
    return (
        <section className="skills-section">
            <h3>SKILLS</h3>
            <div className="skills-container">
                {skills.map((skill) => (
                    <Skill key={skill} skill={skill} />
                ))}
            </div>
        </section>
    );
}
