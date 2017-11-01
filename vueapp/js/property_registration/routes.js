import App from './App'
import Lookup from './views/Lookup'
import Contact from './views/Contact'
import Details from './views/Details'
import Offer from './views/Offer'
import Confirmation from './views/Confirmation'

export default [
  {
    path: '/',
    name: 'Registration',
    component: App,
    children: [
      {
        path: 'lookup',
        name: 'lookup',
        component: Lookup
      },
      {
        path: 'details',
        name: 'details',
        component: Details
      },
      {
        path: 'contact',
        name: 'contact',
        component: Contact
      },
      {
        path: 'offer',
        name: 'offer',
        component: Offer
      },
      {
        path: 'confirmation',
        name: 'confirmation',
        component: Confirmation
      }
    ]
  }
]