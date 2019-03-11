import React, { Component } from 'react';
import Iframe from 'react-iframe';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import axios from 'axios';

import Ambulance from './../images/ambulance.jpeg';
import Logo from './../images/logo.png';
import './../css/landing.css';

class Landing extends Component {
    constructor(props) {
        super(props);
        this.state = {
            hospital: 0,
            location: 34,
        }
    }

    locationChange = (e) => {
        // console.log(e.target.value);
        this.setState({ hospital: e.target.value });
    }
    hospitalChange = (e) => {
        // console.log(e.target.value);
        this.setState({ location: e.target.value })
    }
    getGraph = () => {
        const config = {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        }
        let data = {
            location: this.state.location,
            hospital: this.state.hospital
        }

        let url = 'http://4e7f4c7e.ngrok.io/posts/';

        axios.post(url, data, config)
            .then((result) => {
                console.log(result)
            })
            .catch((err) => {
                console.log(err);
            })
    }
    render() {
        let url = `http://4e7f4c7e.ngrok.io/posts/?location=${this.state.location}&hospital=${this.state.hospital}`
        return (
            <div className="landing-wrapper">
                <Grid container spacing={24}>
                    <Grid item xs={5}>
                        <img src={Logo} alt="logo" className="logo" />
                        <h1 className="landing-head">We Care</h1>
                        <br /><br />
                        <div className="location-select-wrapper">
                            <select className="location-select" onChange={this.hospitalChange}>
                                <option className="location-select-option" value="0">Eye Foundation and Research Center</option>
                                <option className="location-select-option" value="23">Apollo Gleneagles Hospitals</option>
                                <option className="location-select-option" value="31">AMRI Hospitals</option>
                            </select>
                        </div>
                        <br />
                        <br />
                        <div className="location-select-wrapper">
                            <select className="location-select" onChange={this.locationChange}>
                                <option className="location-select-option" value="34">Tangra</option>
                                <option className="location-select-option" value="2">Kankurgachi</option>
                                <option className="location-select-option" value="26">Nicco Park</option>
                                <option className="location-select-option" value="19">Sister Nivedita Statue</option>
                                <option className="location-select-option" value="10">Newtown</option>
                                <option className="location-select-option" value="14">Salt lake Stadium</option>
                                <option className="location-select-option" value="28">Kali Mandir</option>
                                <option className="location-select-option" value="33">LA Block</option>
                            </select>
                        </div>
                        <div className="submit-button">
                            <br /><br />
                            <Button variant="contained" color="primary" onClick={this.getGraph}>
                                Submit
                            </Button>
                        </div>
                    </Grid>
                    <Grid item xs={7}>
                        <Iframe url={url}
                            width="100%"
                            height="100%"
                            id="myId"
                            className="myClassname"
                            display="initial"
                            position="relative"
                        />
                    </Grid>
                </Grid>
                <img src={Ambulance} alt="ambulance" className="amb-img" />
            </div>
        );
    }
}

export default Landing;