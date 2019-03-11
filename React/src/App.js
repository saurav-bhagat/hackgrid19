import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import './App.css';

import Landing from './components/Landing';
import Landing2 from './components/Landing2';

class App extends Component {
	render() {
		return (
			<div className="App">
                <BrowserRouter basename={process.env.PUBLIC_URL}>
                    <Switch>
						<Route exact path="/" component={Landing} />
                        <Route exact path="/try" component={Landing2} />
					</Switch>
                </BrowserRouter>
			</div>
		);
	}
}

export default App;
