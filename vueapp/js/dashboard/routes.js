import App from './App'
import Properties from './views/Properties'
import Settings from './views/Settings'
import ProfileSettings from './views/ProfileSettings'
import SuperhostSettings from './views/SuperhostSettings'
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
        path: 'settings',
        name: 'My Settings',
        component: Settings,
        children: [
          {
            path: 'profile',
            name: 'Edit Profile',
            component: ProfileSettings
          },
          {
            path: 'superhost',
            name: 'Superhost Settings',
            component: SuperhostSettings
          },
          {
            path: 'owner',
            name: 'Owner Settings',
            component: ComingSoon
          },
        ]
      }
    ]
  }
]
