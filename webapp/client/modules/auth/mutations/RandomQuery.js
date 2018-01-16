import { ConnectionHandler } from 'relay-runtime';
import { setToken, setUserName } from '../jwtUtils';
import {getToken, hasValidJwtToken} from "modules/auth/jwtUtils";

/*const {
  commitMutation,
  graphql,
} = require('react-relay');

const mutation = graphql`
    mutation LoginMutation(
    $input: LoginMutationInput!
    ) {
        login(input : $input) {
            authFormPayload{
                    __typename
                    ... on Viewer{
                        tokens{
                            __typename
                            ... on TokensSuccess {
                                token
                            }
                            ... on TokenError {
                                error
                            }
                        }
                    }
                }
        }
    }
`;*/

const tokenName = 'jwtToken';

function RandomQuery(environment, input: {release_date:string}) {
    return fetch(`/resources/videos/randomQuery?user_id=${encodeURIComponent(getToken())}`, {
        method: 'GET',
        credentials: 'same-origin',
        headers: {
            authorization: `Bearer ${hasValidJwtToken().token}`,
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
    });
    /*commitMutation(
      environment,
      {
        mutation,

        onCompleted: response =>
        {setToken(response.login.authFormPayload.tokens.token); console.log(response)},
        variables: {
          input
        },
          onError: error => console.log(error)
      },
    );*/
}

export default RandomQuery;