/* eslint-disable jsx-a11y/href-no-hash */
import React from 'react';
import Page from '../Page/Page';
import '../../../node_modules/react-aspect-ratio/aspect-ratio.css';
import './SearchResults.css';
import AspectRatio from 'react-aspect-ratio';

const subtitleStyle = {
    color: '#fff',
    fontFamily: 'GeosansLight',
    fontWeight: '300',
    fontSize: '20px'
}

const smallFrames = {
    width:'100%',
    margin: 'auto'
}

class SearchResults extends React.Component {
    constructor(props){
        super(props);

        const content = JSON.parse(localStorage.getItem('eqSearchResults'));

        if (localStorage.getItem('jwtToken') === null || localStorage.getItem('jwtToken') === undefined ){
            window.location.replace('/');
        }

        console.log(content);

        if( content !== undefined && content !== null ) {

            const data = content.content.data;
            const subtitle = content.title;
            const limit = data.length % 2 === 1 ? parseInt(data.length / 2) : parseInt((data.length-1)/2)*-1;

            console.log(data);

            this.state = {
                mainResult: data[0],
                results: data.slice(1, parseInt((data.length-1)/2)*2+1),
                subtitle: subtitle === undefined ? '' : subtitle,
            };

            console.log('here2');

        } else {
            this.state = {
                results : [],
                mainResult: ''
            };
        }

        this.searchResults = [];

        for (let i = 0; i < this.state.results.length; i++) {
            this.searchResults.push(
                <div style={{width: (50).toString() + '%', margin : 'auto', display: 'inline-block', minWidth: '300px'}} key={i}>
                <AspectRatio ratio="16/9" style={{width: '90%', margin: 'auto', minWidth: '300px'}}>
                    <iframe src={"http://www.youtube.com/embed/" + this.state.results[i].youtube_video_id} style={{width:'100%', margin: 'auto'}}
                            frameBorder="0" allowFullScreen>
                    </iframe>
                </AspectRatio><br/>
                </div>
            ); console.log(i);
        }

        console.log(this.state);
    }

    render(){
        return (
            <Page heading='Search Results' >
                <div style={{maxWidth: '800px', margin: 'auto', width: '98%', minWidth:'300px'}}>
                <div>
                    <h1 style={subtitleStyle}>
                        {this.state.subtitle}
                    </h1>
                </div>
                <div>
                    <AspectRatio ratio="16/9" style={{maxWidth: '800px', minWidth: '300px'}}>
                        <iframe
                            src={"http://www.youtube.com/embed/" + this.state.mainResult.youtube_video_id}
                            frameBorder="0" allowFullScreen
                            key={'main'}>
                        </iframe>
                    </AspectRatio>
                </div>
                <br/><br/>
                <div style={{width: '100%', margin: 'auto'}}>
                    {this.searchResults}
                </div>
                </div>
            </Page>
        );
    }
}

export default SearchResults;
