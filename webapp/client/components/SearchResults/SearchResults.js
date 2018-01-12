/* eslint-disable jsx-a11y/href-no-hash */
import React from 'react';
import { Player } from '../../../node_modules/video-react';
import Page from '../Page/Page';
import "../../../node_modules/video-react/styles/scss/video-react.scss";


class SearchResults extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            results: [
                {videoTitle: 'Blas', songTitle: 'Blis', youtube_video_id: 'RAsN9OVI-vQ'},
                {videoTitle: 'Blas', songTitle: 'Blis', youtube_video_id: 'RAsN9OVI-vQ'},
                {videoTitle: 'Blas', songTitle: 'Blis', youtube_video_id: 'RAsN9OVI-vQ'},
                {videoTitle: 'Blas', songTitle: 'Blis', youtube_video_id: 'RAsN9OVI-vQ'},
                {videoTitle: 'Blas', songTitle: 'Blis', youtube_video_id: 'RAsN9OVI-vQ'},
                {videoTitle: 'Blas', songTitle: 'Blis', youtube_video_id: 'RAsN9OVI-vQ'},
            ]
        }
        this.searchResults = [];
        //const i = 0;
        for (var i = 0; i < this.state.results.length; i++) {
            this.searchResults.push(
                <iframe src="http://www.youtube.com/embed/W7qWa52k-nE"
                        width="100%" height="100%" frameBorder="0"  key={i} allowFullScreen>
                </iframe>
            );
        }
    }

    render(){
        return (
            <Page heading='Search Results' >
                {this.searchResults}
                <iframe src="http://www.youtube.com/embed/W7qWa52k-nE"
                        width="100%" height="100%" frameBorder="0" allowFullScreen>
                </iframe>
            </Page>
        )
            ;
    }


}

export default SearchResults;
