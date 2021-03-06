import React from 'react';
import { createRefetchContainer, graphql } from 'react-relay';
import Page from 'components/Page/Page';
import styles from './Polls.scss';
import PollsVote from './PollsVote';
import PollsResults from './PollsResults';

const variables = { count: 10 };

class PollDetail extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      id: props.router.match.params.id,
      isLoading: true
    };
  }

  componentWillMount() {
    const variables = { id: this.state.id };
    this.props.relay.refetch(variables, null, () => this.setState({ isLoading: false }));
  }

  _updateState(selected) {
    this.setState({ selected });
  }

  render() {
    const { environment, viewer: { question }, router } = this.props;
    const { isLoading } = this.state;

    return (
      <Page heading='Polls Detail' className={styles.pollDetailRoot} >
        { isLoading ? 'loading' : null }

        { question ?
          <div>
            <h2>Question: {question.questionText}</h2>

            {question.hasViewerVoted ?
              <PollsResults
                environment={environment}
                question={question}
                router={router}
              /> :
              <PollsVote
                environment={environment}
                question={question}
                router={router}
              />
            }

          </div> : 'None Found'
        }
      </Page>
    );
  }
}


export default createRefetchContainer(PollDetail, {
    viewer: graphql.experimental`
      fragment  PollsDetail_viewer on Viewer
       @argumentDefinitions(
            id: {type: "ID!", defaultValue: ""},
        )
      {
          id
          question(id: $id) {
              questionText
              hasViewerVoted
              ...PollsVote_question
              ...PollsResults_question
          }
      }
  `
  },
  graphql.experimental`
        query PollsDetailViewerRefetchQuery(
        $id: ID!,
        ) {
            viewer{
                  ...PollsDetail_viewer @arguments(
                    id: $id
                  )
            }
        }
  `
);

