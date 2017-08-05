import App from './App'
import Properties from './views/Properties'
import ComingSoon from './views/ComingSoon'

export default [
  {
    path: '/',
    name: 'Dashboard',
    redirect: 'properties',
    component: App,
    children: [
      {
        path: 'properties',
        name: 'My Properties',
        component: Properties
      },
      {
        path: 'maintenance',
        name: 'Maintenance Requests',
        component: ComingSoon
      },
      {
        path: 'statements',
        name: 'Rent Statements',
        component: ComingSoon
      },
      {
        path: 'profile',
        name: 'My Profile',
        component: ComingSoon
      },
      {
        path: 'settings',
        name: 'My Settings',
        component: ComingSoon
      }
    ]
  }
]
