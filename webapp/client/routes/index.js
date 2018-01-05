import App from 'components/App/App';
import Landing from 'components/Landing/Landing';
import Vertical from 'components/Vertical/Vertical';
import authRoutes from './auth';
import pollsRoutes from './polls';

const routes = [
  {
    component: App,
    childRoutes: [
      {
        path: '/',
        component: Vertical,
        queries: 'queries'
      },
      ...authRoutes,
      ...pollsRoutes
    ]
  }

];

export default routes;
