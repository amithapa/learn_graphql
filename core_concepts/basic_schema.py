from graphene import ObjectType, String, Schema

class Query(ObjectType):
    # THis defines a Field `hello` in our Schema with a single Argument `name`
    hello = String(name=String(default_value="Stranger"))
    goodbye = String()

    # Our resolver method takes the GraphQL context (root, info) as well as
    # Argument(name) for the field and returns data for the query Response
    def resolve_hello(root, info, name):
        return f"Hello {name}"

    def resolve_goodbye(root, info):
        return "See ya!"

schema = Schema(query=Query)


if __name__ == '__main__':
    query_string = "{ hello goodbye}"
    result = schema.execute(query_string)
    print(result.data["hello"])
    print(result.data["goodbye"])

    query_with_argument = '{ hello(name: "amit")}'
    result = schema.execute(query_with_argument)
    print((result.data["hello"]))