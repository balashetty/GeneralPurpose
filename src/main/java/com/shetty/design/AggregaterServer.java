package com.shetty.design;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Arrays;
import java.util.stream.Collectors;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

@SuppressWarnings("restriction")
public class AggregaterServer {

	public static void main(String[] args) {
		Integer port = null;
		String funcName = null;

		if (Arrays.toString(args).contains("port")) {
			if (args.length < 4) {
				System.out.println("Usage Sample: AggregaterServer --aggregate max --port 8080");
				throw new RuntimeException("Invalid arguments");
			}

			port = Integer.valueOf(args[3]);
			funcName = args[1];
		} else if (args.length < 3) {
			System.out.println("Usage Sample: Aggregater --aggregate max 4 8 3");
			throw new RuntimeException("Invalid arguments");
		}

		System.out.println("Arguments:" + Arrays.toString(args));

		if (port == null) {
			funcName = args[1];
			int[] arr = new int[args.length - 2];

			for (int i = 2; i < args.length; i++) {
				arr[i - 2] = Integer.valueOf(args[i]);
			}

			int res = 0;

			switch (funcName) {
			case "max":
				res = max(arr);
				break;
			case "sum":
				res = sum(arr);
				break;
			default:
				System.err.println("Unknown Aggregater frunction");
				throw new RuntimeException("Invalid arguments");
			}

			System.out.println("Aggregater function name:" + funcName + " and result: " + res);
		} else {
			startServer(port);
			
			try {
				HttpClient client = HttpClient.newHttpClient();
				HttpRequest request = HttpRequest.newBuilder().uri(URI.create("http://localhost:8080?N=1+3+2+1")).build();

				HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
				System.out.println(response.body());
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}

	private static void startServer(int port) {
		try {
			InetSocketAddress isa = new InetSocketAddress("localhost", port);

			HttpServer server = HttpServer.create(isa, 0);
			server.createContext("/", new MyHandler());

			server.start();

			System.out.println("Server started on port " + port);
		} catch (IOException e) {
			System.err.println("failed to start the server " + e.toString());
			e.printStackTrace();
		}

	}

	private static int sum(int[] nums) {
		int res = 0;

		for (int num : nums) {
			res += num;
		}

		return res;
	}

	private static int max(int[] nums) {
		int res = 0;

		for (int num : nums) {
			res = Math.max(num, res);
		}

		return res;
	}

	// define a custom HttpHandler
	static class MyHandler implements HttpHandler {
		@Override
		public void handle(HttpExchange exchange) throws IOException {
			URI uri = exchange.getRequestURI();
			String input = uri.toString().substring(4);
			java.util.List<Integer> numbers = Arrays.stream(input.split("\\+"))
	                .map(Integer::parseInt)
	                .collect(Collectors.toList());

	        int sum =  numbers.stream().reduce(0, Integer::sum);
			System.out.println("uri " + uri + "sum:" + sum);
	
			// handle the request
			String response = String.format("<html>\n" + "<head>\n" + "<title>sum</title>\n" + "</head>\n" + "<body>\n"
					+ "<p>%d</p>\n" + "</body>\n" + "</html>", sum);
			exchange.sendResponseHeaders(200, response.length());
			OutputStream os = exchange.getResponseBody();
			os.write(response.getBytes());
			os.close();
		}
	}

}
