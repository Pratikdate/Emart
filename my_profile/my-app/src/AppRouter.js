import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import index from '.public/index';



function AppRouter() {
    return (
      <Router>
        <Switch>
          <Route exact path="/" component={index} />
          <Route path="/about" component={AboutPage} />
        </Switch>
      </Router>
    );
  }
  
  export default AppRouter;
  