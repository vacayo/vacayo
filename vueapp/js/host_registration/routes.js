import App from './App'
import Agreement from './views/Agreement'

export default [
  {
    path: '/',
    name: 'SuperHostRegistration',
    redirect: 'agreement',
    component: App,
    children: [
      {
        path: 'agreement',
        name: 'Payment Agreement',
        component: Agreement
      }
    ]
  }
]
