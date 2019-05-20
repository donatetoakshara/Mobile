import Login from './container';
import { Route } from './../../app-constants';

export default ({
    routeKey:Route.login,
    navConfig: {

        // placeholder to pass any state , if required so its made as a function
        screen: Login(),
        navigationOptions: {
            header: null
        }
    }
});