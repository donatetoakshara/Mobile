import React, { Component } from 'react';
import { createAppContainer } from 'react-navigation';

import screens from './src/nav/get-screens';
import createNav from './src/nav';

// root component
const Root = createNav(screens);
const AppContainer = createAppContainer(Root);

export default () => <AppContainer />;
