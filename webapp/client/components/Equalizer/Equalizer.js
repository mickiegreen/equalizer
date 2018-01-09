import React from 'react';
import Page from '../../components/Page/Page';
import styles from '../../styles/equalizer.origin.scss';

class Equalizer extends React.Component {
    onChange = (value) => {
        console.log(value)
    }

    render() {
        return(
            <Page heading='Equalizer'>
                <section>
                    <input type='range' min='-12' value='4.5' max='12' step='.1' onChange={this.onChange}/>
                    <input type='range' min='-12' value='4' max='12' step='.1' onChange={this.onChange}/>
                    <input type='range' min='-12' value='2' max='12' step='.1' onChange={this.onChange}/>
                    <input type='range' min='-12' value='1' max='12' step='.1' onChange={this.onChange}/>
                    <input type='range' min='-12' value='-1' max='12' step='.1' onChange={this.onChange}/>
                    <input type='range' min='-12' value='-1.5' max='12' step='.1' onChange={this.onChange}/>
                    <input type='range' min='-12' value='.5' max='12' step='.1' onChange={this.onChange}/>
                    <input type='range' min='-12' value='2' max='12' step='.1' onChange={this.onChange}/>
                    <input type='range' min='-12' value='3' max='12' step='.1' onChange={this.onChange}/>
                    <input type='range' min='-12' value='4' max='12' step='.1' onChange={this.onChange}/>
                </section>
            </Page>
        );
    }
}

export default Equalizer;

