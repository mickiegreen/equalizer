import Auth from '../modules/auth/Auth';
import Vertical from "components/Vertical/Vertical";
import Landing from "components/Landing/Landing";
import SearchResults from "components/SearchResults/SearchResults";
import History from "components/History/History";

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
    {
        path: '/history',
        component: History,
    },
];


export default authRoutes;
