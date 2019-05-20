import Profile from './container';
import { Route } from './../../app-constants';

export default ({
    routeKey:Route.profile,
    navConfig: {
        screen: Profile(),
        navigationOptions: {
            title:'Profile',
            header: null
        }
    }
});