import App from 'components/App/App';
import authRoutes from './auth';
import pollsRoutes from './polls';
import Home from "components/Home/Home";

const routes = [
  {
    component: App,
    childRoutes: [
      {
        path: '/',
        component: Home,
        queries: 'queries'
      },
      ...authRoutes,
      ...pollsRoutes
    ]
  }

];

export default routes;
