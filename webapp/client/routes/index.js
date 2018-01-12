import App from 'components/App/App';
import Landing from 'components/Landing/Landing';
import Vertical from 'components/Vertical/Vertical';
import authRoutes from './auth';
import pollsRoutes from './polls';
import Profile from 'modules/auth/Profile/Profile';
import SearchResults from "components/SearchResults/SearchResults";
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
        {
            path: '/profile',
            component: Profile,
            queries: 'queries'
        },
      ...authRoutes,
      ...pollsRoutes
    ]
  }

];

export default routes;
