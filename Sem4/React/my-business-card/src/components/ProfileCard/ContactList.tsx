interface ContactListProps{
    phone: string
    email: string
    website: string
}

export default function ContactList({phone,email,website}: ContactListProps)
{
    return (
        <ul className="contact-list">
            <li>{phone}</li>
            <li>{email}</li>
            <li>{website}</li>
        </ul>
    );
}