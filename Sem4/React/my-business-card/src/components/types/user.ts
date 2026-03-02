export interface UserProfile {
    avatar: string;
    name: string;
    title: string;
    company: string;
    contact : {
        phone: string;
        email: string;
        website: string;
    };
    about: string;
    skills: string[];

}