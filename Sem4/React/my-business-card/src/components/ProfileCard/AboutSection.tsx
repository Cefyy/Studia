import './AboutSection.css';

interface AboutSectionProps {
    about: string;
}

export default function AboutSection({ about }: AboutSectionProps) {
    return (
        <section className="about-section">
            <h3>ABOUT ME</h3>
            <p>{about}</p>
        </section>
    );
}
