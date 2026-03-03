import type {UserProfile} from "../types/user";
import ProfileHeader from "./ProfileHeader";
import ContactList from "./ContactList";
import AboutSection from "./AboutSection";
import SkillsList from "./SkillsList";
import Divider from "./Divider";
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

            <Divider />

            <ContactList
                phone={user.contact.phone}
                email={user.contact.email}
                website={user.contact.website}
            />
            
            <Divider />

            <AboutSection about={user.about} />

            <SkillsList skills={user.skills} />
        </article>
    )
}
