import React, { Component } from 'react'
import Slider from 'react-rangeslider'
import '../../styles/slider.scss'
import Page from '../../components/Page/Page'

const DATA = {
    name: 'John Smith',
    imgURL: 'http://lorempixel.com/100/100/',
    hobbyList: ['coding', 'writing', 'skiing']
}
const ProfileApp = () =>
    <div>
        <Profile
            name='name'
            imgURL='url'/>
        <Hobbies
            hobbyList='list' />
    </div>

const Profile = () =>
    <div>
        <h3>name</h3>
        <img src={''} />
    </div>

const Hobbies = React.createClass({
    render: function(){
        const hobbies = this.props.hobbyList.map(function(hobby, index){
            return (<li key={index}>{hobby}</li>);
        });
        return (
            <div>
                <h5>My hobbies:</h5>
                <ul>

                </ul>
            </div>
        );
    }
});
export default ProfileApp