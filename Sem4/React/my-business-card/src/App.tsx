import ProfileCard from './components/ProfileCard/ProfileCard'
import type { UserProfile } from './components/types/user'
import avatarImage from './assets/istockphoto-1051202402-612x612.jpg'



const mockUser : UserProfile = {
  avatar : avatarImage,
  name: 'John Doe',
  title: 'Software Engineer',
  company: 'ABC LLC',
  contact: {
    phone: '+48 123 456 789',
    email: 'john.does@example.com',
    website: 'www.johndoe.dev'
  },
  about: 'Passionate engineer with over 8 years of experience in building scalable web applications. I specialize in React ecosystems and performance optimization, always focusing on delivering clean, maintainable code and exceptional user experiences.',
  skills: ['React.js', 'TypeScript', 'Frontend Development', 'UI/UX Design', 'Project Management', 'Agile']
}

export default function App()
{
  return(
    <main className='app-container'>
        <ProfileCard user={mockUser}/>
    </main>
  );
}
