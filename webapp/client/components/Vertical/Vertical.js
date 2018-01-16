import React, { Component } from 'react'
import Slider from 'react-rangeslider'
import '../../styles/slider.scss'
import Page from '../../components/Page/Page'
import Button from 'react-mdc-web/lib/Button/Button';
import './Vertical.css';
import {hasValidJwtToken, getToken} from "modules/auth/jwtUtils";

const equalizerSlider = {
    display: 'inline-block',
    width: '25%'
}

const EQBtnStyleRight = {
    margin: 'auto',
    borderColor: '#fff',
    border: '2px solid #fff',
    borderRadius: '6px',
    width: '48%',
    maxWidth: '100px',
}

const centered = {
    margin: 'auto',
    width: '100%',
    maxWidth: '500px'
}

const ButtonFont = {
    fontWeight:'650',
    color: '#fff',
    //paddingLeft: '44px'
    textAlign: 'center',
    margin: 'auto',
    width: '100%',
    fontFamily: 'GeosansLight',
    letterSpacing: '2px',
    backgroundColor: '#3b0e5478'
}

const ButtonFont2 = {
    fontWeight:'600',
    color: '#fff',
    //paddingLeft: '44px'
    textAlign: 'center',
    margin: 'auto',
    width: '100%',
    fontFamily: 'GeosansLight',
    letterSpacing: '2px',
    fontSize: '20px'
}



class Vertical extends React.Component {
    constructor(props: Object) {
        super(props);
        console.log(props.history);
        this.state = {
            likes: 50,
            views: 50,
            dislikes: 50,
            comments: 50,
            currentMode: 'random',
            modes: ['random', 'update']
        };
    }

    state: { value: number, reverseValue: number };

    handleLikesChange = (value) => {
        this.setState({
            likes: value
        })
    }

    handleDisikesChange = (value) => {
        this.setState({
            dislikes: value
        })
    }

    handleViewsChange = (value) => {
        this.setState({
            views: value
        })
    }

    handleCommentsChange = (value) => {
        this.setState({
            comments: value
        })
    }

    handleClicked = (value) => {
        console.log("handleClicked");
        console.log("randomQuery");
        fetch(`/resources/videos/customQuery?user_id=${encodeURIComponent(getToken())}&likes=${encodeURIComponent(this.state.likes)}&dislikes=${encodeURIComponent(this.state.dislikes)}&comments=${encodeURIComponent(this.state.comments)}&views=${encodeURIComponent(this.state.views)}`, {
            method: 'GET',
            credentials: 'same-origin',
            headers: {
                authorization: `Bearer ${hasValidJwtToken().token}`,
                Accept: 'application/json',
                'Content-Type': 'application/json',
            }}).then(response => {
                this.props.history.push({
                    pathname : '/search',
                    data: response.content
                });
        });
    }

    render() {
        const { likes, dislikes, views, comments } = this.state
        const mode = 'random';
        return (
            <div style={centered}>
            <div className='slider orientation-reversed'>
                <div className='slider-group' style={equalizerSlider}>
                    <div className='slider-vertical'>
                        <h1 style={ButtonFont2}>likes</h1>
                        <Slider
                            min={0}
                            max={100}
                            value={likes}
                            orientation='vertical'
                            onChange={this.handleLikesChange}
                        />
                        <div className='value'>{likes/100}</div>
                    </div>
                </div>
                <div className='slider-group' style={equalizerSlider}>
                    <div className='slider-vertical'>
                        <h1 style={ButtonFont2}>dislikes</h1>
                        <Slider
                            min={0}
                            max={100}
                            value={dislikes}
                            orientation='vertical'
                            onChange={this.handleDisikesChange}
                        />
                        <div className='value'>{dislikes/100}</div>
                    </div>
                </div>
                <div className='slider-group' style={equalizerSlider}>
                    <div className='slider-vertical'>
                        <h1 style={ButtonFont2}>views</h1>
                        <Slider
                            min={0}
                            max={100}
                            value={views}
                            orientation='vertical'
                            onChange={this.handleViewsChange}
                        />
                        <div className='value'>{views/100}</div>
                    </div>
                </div>
                <div className='slider-group' style={equalizerSlider}>
                    <div className='slider-vertical'>
                        <h1 style={ButtonFont2}>comments</h1>
                        <Slider
                            min={0}
                            max={100}
                            value={comments}
                            orientation='vertical'
                            onChange={this.handleCommentsChange}
                        />
                        <div className='value'>{comments/100}</div>
                    </div>
                </div>
            </div>
                <div style={EQBtnStyleRight}>
                    <Button
                        primary
                        className='button_submit-login-form'
                        onClick={this.handleClicked}
                        display={'inline-block'}
                        style={ButtonFont}
                    >Submit</Button>
                </div>
            </div>
        );
    }


}

export default Vertical