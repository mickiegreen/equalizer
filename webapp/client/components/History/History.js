/* eslint-disable jsx-a11y/href-no-hash */
import React from 'react';
import { Player } from '../../../node_modules/video-react';
import Page from '../Page/Page';
/*import "../../../node_modules/video-react/styles/scss/video-react.scss";*/
import '../../../node_modules/react-aspect-ratio/aspect-ratio.css';
import styles from './History.css';
import AspectRatio from 'react-aspect-ratio';
import '../../modules/auth/mutations/RandomQuery';

const frameStyle = {
    margin: 'auto',
    padding: '10px',
    borderColor: 'rgb(0, 0, 0)',
    borderWidth: '10px',
    width: '100%',
}

const mainFrameStyle = {
    margin: 'auto',
    display: 'block',
    padding: '4%',
    backgroundColor: 'rgba(0,0,0,.37)',
    border: '2px solid #ffffff',
    borderRadius: '6px'
}

const wrapperFrameStyle = {
    border: '2px solid #ffffff',
    borderRadius: '6px'
}

class History extends React.Component {

    constructor(props){
        super(props);
        console.log(localStorage.getItem('jwtToken') );
        if (localStorage.getItem('jwtToken') === null || localStorage.getItem('jwtToken') === undefined ){
            // todo - ADD NEXT LINE
            window.location.replace('/');
            console.log(localStorage.getItem('jwtToken'));
            console.log(localStorage.getItem('jwtToken') === undefined );
        }
        this.state = {
            mainResult: {videoTitle: 'Blas', youtube_video_id: 'RAsN9OVI-vQ'},
            results: [
                {videoTitle: 'Blas', youtube_video_id: 'RAsN9OVI-vQ'},
                {videoTitle: 'Blas', youtube_video_id: 'RAsN9OVI-vQ'},
                {videoTitle: 'Blas', youtube_video_id: 'RAsN9OVI-vQ'},
                {videoTitle: 'Blas', youtube_video_id: 'RAsN9OVI-vQ'},
            ],
            subtitle: props.randomResults === undefined ? '' : 'You got ' + props.randomResults,
        }
        this.searchResults = [];
        //const i = 0;
        for (let i = 0; i < this.state.results.length; i++) {
            this.searchResults.push(
                <div style={{width:'25%', margin : 'auto', display: 'inline-block'}} key={i + 100}>
                <AspectRatio ratio="16/9" style={{maxWidth: '84%', margin: 'auto'}}>
                    <iframe src="http://www.youtube.com/embed/W7qWa52k-nE" style={{width:'100%', margin: 'auto'}}
                            frameBorder="0"  allowFullScreen>
                    </iframe>
                </AspectRatio>
                </div>
            );
        }
    }

    render(){
        return (
            <Page heading='Your History' >
                <div>
                    <h1>
                        {this.state.subtitle}
                    </h1>
                </div>
                <div>
                    <AspectRatio ratio="16/9" style={{maxWidth: '1000px', minWidth:'100%'}}>
                        <iframe
                            src="http://www.youtube.com/embed/W7qWa52k-nE"
                            frameBorder="0" allowFullScreen
                            key={'main'}>
                        </iframe>
                    </AspectRatio>
                </div><br/><br/>
                <div style={{width: '100%', margin : 'auto'}} >
                    {this.searchResults}
                </div>
            </Page>
        );
    }
}

export default History;
