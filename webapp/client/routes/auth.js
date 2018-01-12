import Auth from '../modules/auth/Auth';
import Vertical from "components/Vertical/Vertical";
import Landing from "components/Landing/Landing";
import SearchResults from "components/SearchResults/SearchResults";
//import Equalizer from "components/Equalizer/Equalizer";


const authRoutes = [
  {
    path: '/signup',
    component: Auth,
  },
  {
    path: '/login',
    component: Auth,
  },
    {
        path: '/home',
        component: Landing,
    },
    {
        path: '/equalizer',
        component: Vertical,
    },
    {
        path: '/search',
        component: SearchResults,
    },
];


export default authRoutes;
