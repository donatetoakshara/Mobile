import {
    createStackNavigator,
    createSwitchNavigator
}
    from 'react-navigation';

export default ({ login, profile }) => createSwitchNavigator(
    {
        [login.routeKey]: login.navConfig,
        [profile.routeKey]: profile.navConfig,
    }
);

