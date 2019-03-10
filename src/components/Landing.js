import React, { Component } from 'react';
import Grid from '@material-ui/core/Grid';

import Ambulance from './../images/ambulance.jpeg';
import Logo from './../images/logo.png';
import './../css/landing.css';

class Landing extends Component{

    render(){
        return(
            <div className="landing-wrapper">
                <Grid container spacing={24}>
                    <Grid item xs={5}>
                        <img src={Logo} alt="logo" className="logo" />
                        <h1 className="landing-head">We Care</h1>
                    </Grid>
                    <Grid item xs={7}>
                        <img src={Ambulance} alt="ambulance" className="amb-img" />
                    </Grid>
                </Grid>
            </div>
        );
    }
}

export default Landing;