interface ProfileHeaderProps {
    avatar: string;
    name: string;
    title: string;
    company: string;
}
export default function ProfileHeader( {avatar,name,title,company} : ProfileHeaderProps)
{
    return (
        <header className = "profile-header">
            <div className= "avatar-wrapper">
                <img src={avatar} alt= {`Avatar of &{name}`} className="avatar"/>
            </div>
            <h1 className="name">{name}</h1>
            <h2 className="title">{title}</h2>
            <p className="company">{company}</p>
        </header>
    );
}