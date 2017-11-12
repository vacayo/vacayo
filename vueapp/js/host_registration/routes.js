import App from './App'
import Index from './views/Index'
import Registration from './views/Registration'
import Agreement from './views/Agreement'
import Settings from './views/Settings'

export default [
  {
    path: '/',
    name: 'SuperHostRegistration',
    component: App,
    redirect: 'index',
    children: [
      {
        path: 'index',
        name: 'Become A Superhost',
        component: Index
      },
      {
        path: 'registration',
        name: 'Superhost Registration',
        component: Registration
      },
      {
        path: 'agreement',
        name: 'Superhost Agreement',
        component: Agreement
      },
      {
        path: 'Settings',
        name: 'Superhost Settings',
        component: Settings
      }
    ]
  }
]
