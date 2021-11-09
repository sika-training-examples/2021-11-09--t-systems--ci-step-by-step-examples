FROM golang as build
WORKDIR /build
COPY hello.go .
ENV CGO_ENABLED=0
RUN go build hello.go

FROM scratch
COPY --from=build /build/hello /
CMD [ "/hello" ]
