import Auth from '../modules/auth/Auth';
import Vertical from "components/Vertical/Vertical";
import Landing from "components/Landing/Landing";
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
    }
];


export default authRoutes;
