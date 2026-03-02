interface SkillProps {
    skill : string;
}

export default function Skill({skill}: SkillProps)
{
    return (
        <span className = "skill">
            {skill}
        </span>
    );
}