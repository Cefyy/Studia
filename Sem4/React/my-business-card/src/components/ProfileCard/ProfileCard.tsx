import type {UserProfile} from "../types/user";
import ProfileHeader from "./ProfileHeader";
import ContactList from "./ContactList";
import Skill from "./Skill";
import './ProfileCard.css';


interface ProfileCardProps {
    user: UserProfile;
}

export default function ProfileCard({user}: ProfileCardProps)
{
    return (
        <article className="profile-card">

            <ProfileHeader
                avatar={user.avatar}
                name={user.name}
                title={user.title}
                company={user.company}
            />

            <hr className="divider"/>

            <ContactList
                phone={user.contact.phone}
                email={user.contact.email}
                website={user.contact.website}
            />
            <hr className="divider"/>

            <section className="about-section">
                <h3> ABOUT ME</h3>
                <p>{user.about}</p>
            </section>

            <section className="skills-section">
                <h3>SKILLS</h3>
                <div className="skills-container">
                    {user.skills.map((skill) => (<Skill key ={skill} skill={skill}/>))}
                </div>
            </section>
        </article>
    )
}
