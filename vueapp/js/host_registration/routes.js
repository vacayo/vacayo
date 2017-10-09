import App from './App'
import Index from './views/Index'
import Agreement from './views/Agreement'
import Congrats from './views/Congrats'


export default [
  {
    path: '/',
    name: 'SuperHostRegistration',
    redirect: 'index',
    component: App,
    children: [
      {
        path: 'index',
        name: 'Become A Superhost',
        component: Index
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
