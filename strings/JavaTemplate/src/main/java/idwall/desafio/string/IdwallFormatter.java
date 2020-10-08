package idwall.desafio.string;

import java.util.ArrayList;
import java.util.List;

public class IdwallFormatter implements StringFormatter {

    public IdwallFormatter(int lineCharLimit, boolean shouldJustify) {
        this.lineCharLimit = lineCharLimit;
        this.shouldJustify = shouldJustify;
    }

    public final int lineCharLimit;
    public final boolean shouldJustify;

    /**
     * {@inheritDoc}
     */
    @Override
    public String format(String text) {
        final List<String> justifiedLines = new ArrayList<>();

        String[] words = text.split(" ");

        int length = words.length;
        int i = 0;

        while (i < length) {
            int start = i;
            int lineLength = words[i].length();
            int count = 0;

            while (i + 1 < length && lineLength + words[i + 1].length() + count < lineCharLimit) { //should have one more word
                i++;
                count++;
                lineLength += words[i].length();
            }

            final StringBuilder stringBuilder = new StringBuilder();

            for (int j = start; j <= i; j++) {
                stringBuilder.append(words[j]);

            }
            justifiedLines.add(stringBuilder.toString());
            i++;
        }

        return String.join("\n", justifiedLines);
    }


}
