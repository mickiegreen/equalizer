/* eslint-disable jsx-a11y/href-no-hash */
import React from 'react';
import { Player } from '../../../node_modules/video-react';
import Page from '../Page/Page';
import "../../../node_modules/video-react/styles/scss/video-react.scss";


class Home extends React.Component {

    render() {
        return (
            <Page heading='' >
                <iframe src="http://www.youtube.com/embed/W7qWa52k-nE"
                        width="100%" height="100%" frameBorder="0" allowFullScreen>
                </iframe>
            </Page>
        )
            ;
    }


}

export default Home;
