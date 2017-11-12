import App from './App'
import Index from './views/Index'
import Register from './views/Register'
import Agreement from './views/Agreement'
import Congrats from './views/Congrats'


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
        path: 'register',
        name: 'Superhost Registration',
        component: Register
      },
      {
        path: 'agreement',
        name: 'Payment Agreement',
        component: Agreement
      },
      {
        path: 'congrats',
        name: 'Congratulations',
        component: Congrats
      }
    ]
  }
]
