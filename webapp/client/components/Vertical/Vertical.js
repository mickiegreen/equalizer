import React, { Component } from 'react'
import Slider from 'react-rangeslider'
import '../../styles/slider.scss'
import Page from '../../components/Page/Page'
import Button from 'react-mdc-web/lib/Button/Button';

const equalizerSlider = {
    display: 'inline-block',
    width: '20%'
}

const centered = {
    margin: 'auto',
    width: '100%',
    maxWidth: '500px'
}

class Vertical extends React.Component {
    constructor(props: Object) {
        super(props);
        this.state = {
            value: 25,
            reverseValue: 8,
            currentMode: 'random',
            modes: ['random', 'update']
        };
    }

    state: { value: number, reverseValue: number };

    handleChange = (value) => {
        this.setState({
            value: value
        })
    }

    handleChangeReverse = (value) => {
        this.setState({
            reverseValue: value
        })
    }

    render() {
        const { value, reverseValue } = this.state
        const mode = 'random';
        return (
            <div style={centered}>
            <div className='slider orientation-reversed'>
                <div className='slider-group' style={equalizerSlider}>
                    <div className='slider-vertical'>
                        <Slider
                            min={0}
                            max={1}
                            value={value}
                            orientation='vertical'
                            onChange={this.handleChange}
                        />
                        <div className='value'>{value}</div>
                    </div>
                </div>
                <div className='slider-group' style={equalizerSlider}>
                    <div className='slider-vertical'>
                        <Slider
                            min={0}
                            max={1}
                            value={value}
                            orientation='vertical'
                            onChange={this.handleChange}
                        />
                        <div className='value'>{value}</div>
                    </div>
                </div>
                <div className='slider-group' style={equalizerSlider}>
                    <div className='slider-vertical'>
                        <Slider
                            min={0}
                            max={1}
                            value={value}
                            orientation='vertical'
                            onChange={this.handleChange}
                        />
                        <div className='value'>{value}</div>
                    </div>
                </div>
                <div className='slider-group' style={equalizerSlider}>
                    <div className='slider-vertical'>
                        <Slider
                            min={0}
                            max={1}
                            value={value}
                            orientation='vertical'
                            onChange={this.handleChange}
                        />
                        <div className='value'>{value}</div>
                    </div>
                </div>
                <div className='slider-group' style={equalizerSlider}>
                    <div className='slider-vertical'>
                        <Slider
                            min={0}
                            max={1}
                            value={reverseValue}
                            orientation='vertical'
                            onChange={this.handleChangeReverse}
                        />
                        <div className='value'>{reverseValue}</div>
                    </div>
                </div>
            </div>
            </div>
        );
    }


}

export default Vertical